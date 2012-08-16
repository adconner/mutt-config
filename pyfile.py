import re

mapping = { 'INBOX':              'INBOX'
          , '[Gmail]/All Mail':   'all-mail'
          , '[Gmail]/Drafts':     'drafts'
          , '[Gmail]/Important':  'important'
          , '[Gmail]/Sent Mail':  'sent-mail'
          , '[Gmail]/Spam':       'spam'
          , '[Gmail]/Starred':    'starred'
          , '[Gmail]/Trash':      'trash'
          }

r_mapping = { val: key for key, val in mapping.items() }

def nt_remote(folder):
    try:
        return mapping[folder]
    except:
        return re.sub(' ', '-', folder)

def nt_local(folder):
    try:
        return r_mapping[folder]
    except:
        return re.sub('-', ' ', folder)

# folderfilter = exclude(['Label', 'Label', ... ])
def exclude(excludes):
    def inner(folder):
        try:
            excludes.index(folder)
            return False
        except:
            return True

    return inner
