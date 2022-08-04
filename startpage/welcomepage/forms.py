from django import forms


class ticketForm(forms.Form):
    DEFAULT_QUEUES = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )
    TARGET_QUEUES = (
        ("1", "PL.Bridge.BE.Events"),
        ("2", "RO.EOC.Webservices.Windows.1LS"),
        ("3", "PL.Network.1LS"),
        ("4", "PL.Bridge.VO"),
        ("5", "PL.Network.BE.1LS"),
    )

    SLA_SCHEDULE = (
        ("1", "BE 8.00-18.00"),
        ("2", "24*7*365"),
    )

    CI_name = forms.CharField(max_length=100)
    default_queue = forms.ChoiceField(choices=DEFAULT_QUEUES)
    target_queue = forms.ChoiceField(choices=TARGET_QUEUES)
    SLA_schedule = forms.ChoiceField(choices=SLA_SCHEDULE)
    short_description = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)


class newQueueForm(forms.Form):
    formQueueName = forms.CharField(max_length=100)

