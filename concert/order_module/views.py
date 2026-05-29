from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest
from .models import Order, OrderDetail
from ticketSales.models import concertModel, timeModel
from datetime import datetime
from django.http import JsonResponse


def add_to_order(request: HttpRequest):
    concert_id = request.GET.get('concert_id')
    count_seats = request.GET.get('seat')

    if request.user.is_authenticated:
        concert = concertModel.objects.filter(id=concert_id).first()

        if concert is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)
            current_order_details = current_order.details.filter(concert=concert).first()

            if current_order_details is not None:
                return JsonResponse({
                    'status': 'warning',
                    'text': 'the concert already exists in the cart',
                    'confirm_button_text': 'Ok',
                    'icon': 'warning'

                })
            else:
                seats = timeModel.objects.filter(pk=concert_id).first()
                if seats is not None:
                    try:
                        count_seats = int(count_seats)
                    except ValueError:
                        return JsonResponse({
                            'status': 'error',
                            'text': 'Invalid seat count.',
                            'confirm_button_text': 'Ok',
                            'icon': 'error'
                        })

                    if count_seats > seats.Seats:
                        return JsonResponse({
                            'status': 'warning',
                            'text': 'Not enough seats available.',
                            'confirm_button_text': 'Okk!',
                            'icon': 'warning'
                        })

                    new_detail = OrderDetail(order=current_order, concert=concert,
                                             seats=seats, seat_count=count_seats)
                    new_detail.save()

                    seats.Seats -= count_seats
                    seats.save()

                    return JsonResponse({
                        'status': 'success',
                        'text': 'Successfully add concert to Card!',
                        'confirm_button_text': 'Ok',
                        'icon': 'success'
                    })
                else:
                    return JsonResponse({
                        'status': 'no_time_available',
                        'text': 'No time available for this concert.',
                        'confirm_button_text': 'Ok',
                        'icon': 'error'
                    })
        else:
            return JsonResponse({
                'status': 'error',
                'text': 'Concert not found.',
                'confirm_button_text': 'thanks',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'User is not authenticated.',
            'confirm_button_text': 'authenticated',
            'icon': 'warning'
        })


@login_required
def cart_detail(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    context = {
        'order': order,
        'details': order.details.all() if order else [],
    }
    return render(request, 'order_module/cart_detail.html', context)


@login_required
def remove_from_cart(request, detail_id):
    order_detail = get_object_or_404(OrderDetail, id=detail_id,
                                     order__user=request.user, order__is_paid=False)
    order_detail.delete()
    return redirect('cart_detail')


@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if not order or not order.details.exists():
        return redirect('cart_detail')

    total_price = order.total_price
    payment_url = f"https://example.com/payment/start/?amount={total_price}&user={request.user.id}"
    return redirect(payment_url)


@login_required
def payment_callback(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if order:
        order.is_paid = True
        order.payment_date = datetime.now()
        order.save()
    return redirect('cart_detail')
