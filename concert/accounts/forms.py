from django import forms
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    # Add fields for ProfileModel (profile image, gender, credit)
    GENDER_CHOICES = [(1, 'Male'), (2, 'Female')]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    ProfileImage = forms.ImageField(required=False)
    credit = forms.IntegerField(min_value=0, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding 'input100' class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' input100'

    def save(self, commit=True):
        # Save the user instance first
        user = super().save(commit=False)
        if commit:
            user.save()

        # Now save the profile data
        profile = ProfileModel.objects.create(
            user=user,  # Associate the ProfileModel with the created User
            Gender=self.cleaned_data['gender'],  # Gender is an integer (1 or 2)
            credit=self.cleaned_data['credit'] if self.cleaned_data.get(
                'credit') else 0,  # Default credit to 0
            ProfileImage=self.cleaned_data['ProfileImage'],  # Save profile image
        )

        return user


class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = ProfileModel
        fields = ['ProfileImage', 'credit', 'Gender']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['ProfileImage', 'credit', 'Gender']

    # Customizing form fields to add 'input100' class
    ProfileImage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input100'}))
    credit = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input100'}))
    # Gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'input100'}))


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']

    # Removing password field
    password = None

    # Customizing form fields to add 'input100' class
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100'}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='Password ',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='Re_Enter_Password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
