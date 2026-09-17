from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your name",
                "class": (
                    "w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 "
                    "text-gray-100 placeholder-gray-500 focus:outline-none "
                    "focus:ring-2 focus:ring-amber-500"
                ),
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "class": (
                    "w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 "
                    "text-gray-100 placeholder-gray-500 focus:outline-none "
                    "focus:ring-2 focus:ring-amber-500"
                ),
            }
        )
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject",
                "class": (
                    "w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 "
                    "text-gray-100 placeholder-gray-500 focus:outline-none "
                    "focus:ring-2 focus:ring-amber-500"
                ),
            }
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your message",
                "rows": 5,
                "class": (
                    "w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 "
                    "text-gray-100 placeholder-gray-500 focus:outline-none "
                    "focus:ring-2 focus:ring-amber-500"
                ),
            }
        )
    )
