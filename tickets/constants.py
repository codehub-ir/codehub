'''
This file contains all sort of data/configs
that are beings used in the main application
'''

from django.utils.translation import gettext as _

# verification choices for Ticket
# and Comment is_verified
VERIFICATIONS = (
    ('rejected', _('Reject')),
    ('approved', _('Approve')),
    ('pending', _('Pending')),
)