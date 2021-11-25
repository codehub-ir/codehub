'''
This file contains all sort of data/configs
that are beings used in the main application
'''

from django.utils.translation import gettext as _


# lang choices for Snippet.lang
LANGUAGES = (
    ('arduino', 'Arduino'),      # + icon
    ('bash', 'Bash'),            # + icon
    ('c', 'C'),                  # + icon
    ('cpp', 'C++'),              # + icon
    ('csharp', 'C#'),            # + icon
    ('css', 'CSS'),              # + icon
    ('dart', 'Dart'),            # + icon
    ('docker', 'DockerFile'),    # + icon
    ('go', 'Go'),                # + icon
    ('html', 'HTML'),            # + icon
    ('java', 'Java'),            # + icon
    ('js', 'JavaScript'),        # + icon
    ('json', 'JSON'),            # + icon
    ('lua', 'Lua'),              # + icon
    ('md', 'markdown'),          # + icon
    ('mysql', 'MySQL'),          # + icon
    ('php', 'PHP'),              # + icon
    ('python', 'Python'),        # + icon
    ('rb', 'Ruby'),              # + icon
)

# verification choices for Ticket
# and Comment is_verified
VERIFICATIONS = (
    ('rejected', _('Reject')),
    ('approved', _('Approve')),
    ('pending', _('Pending')),
)
