from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm


def feedback(request):
    template_name = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        text = form.cleaned_data['text']
        message_header = text.split()[0]
        for word in text.split()[1:]:
            if len(message_header + word) <= 32:
                message_header += ' ' + word
            else:
                break
        send_mail(
            message_header,
            text,
            'from@example.com',
            ['to@example.com'],
            fail_silently=True,
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
