"""Translations of the program interface in English"""


TITLE_KEYS_GENERAL = "GENERAL KEYBINDINGS"
TITLE_KEYS_CALENDAR = "CALENDAR KEYBINDINGS"
TITLE_KEYS_JOURNAL  = "JOURNAL KEYBINDINGS"

KEYS_GENERAL = {
        ' Space ': 'Switch between calendar and journal',
        '   /   ': 'Toggle split screen',
        '   *   ': 'Toggle global privacy',
        '   ?   ': 'Toggle this help',
        '   q   ': 'Quit',
        }

KEYS_CALENDAR = {
        '  a(A) ': 'Add a (recurring) event',
        '  n,🠒  ': 'Next month (day)',
        '  p,🠐  ': 'Previous month (day)',
        '  d,x  ': 'Delete an event',
        '  e,c  ': 'Edit an event',
        '   m   ': 'Move event',
        '   g   ': 'Go to a certain day',
        '   h   ': 'Toggle event as high priority',
        '   l   ': 'Toggle event as low priority',
        '   .   ': 'Toggle event privacy',
        '   C   ': 'Import events from calcurse',
        '   G   ': 'Return to current month (day)',
        }

KEYS_TODO = {
        '  a(A) ': 'Add new (sub)task',
        '  h(H) ': 'Toggle one (all) of the tasks as high priority',
        '  l(L) ': 'Toggle one (all) of the tasks as low priority',
        '  v(V) ': 'Toggle one (all) of the tasks as done',
        '  u(U) ': 'Unmark one (all) of the tasks',
        '  d(D) ': 'Delete one (all) of the tasks (with all subtasks)',
        '  t(T) ': 'Start/pause (remove) timer for a task',
        '  e,c  ': 'Edit a task',
        '   s   ': 'Toggle between task and subtask',
        '   .   ': 'Toggle task privacy',
        '   m   ': 'Move a task',
        '  C(W) ': 'Import tasks from calcurse (taskwarrior)',
        }

MSG_NAME          = "CALCURE"
MSG_VIM           = "Vim keys (j, k, ZZ, ZQ) work as well!"
MSG_INFO          = "For more information, visit:"
MSG_SITE          = "https://github.com/anufrievroman/calcure"
MSG_EXIT          = "Really exit? (y/n) "

MSG_EVENT_HIGH    = 'Mark as "high priority" event number: '
MSG_EVENT_LOW     = 'Mark as "low priority" event number: '
MSG_EVENT_RESET   = 'Reset status for event number: '
MSG_EVENT_DEL     = 'Delete event number: '
MSG_EVENT_REN     = 'Rename event number: '
MSG_NEW_TITLE     = 'Enter new title: '
MSG_EVENT_MOVE    = 'Move event number: '
MSG_EVENT_MOVE_TO = 'Move event to: '
MSG_EVENT_DATE    = 'Enter date: '
MSG_EVENT_TITLE   = 'Enter title: '
MSG_EVENT_REP     = "How many times repeat the event: "
MSG_EVENT_FR      = "Repeat the event every (d)ay, (w)eek, (m)onth or (y)ear? "
MSG_EVENT_IMP     = "Import events from Calcurse? (y/n)"
MSG_EVENT_PRIVACY = "Toggle privacy of event number: "
MSG_TM_ADD        = 'Add/pause timer for task number: '
MSG_TM_RESET      = 'Remove timer for the task number: '
MSG_TS_HIGH       = 'Mark as "high priority" the task number: '
MSG_TS_LOW        = 'Mark as "low priority" the task number: '
MSG_TS_RES        = 'Reset status for the task number: '
MSG_TS_DONE       = 'Mark as "done" the task number: '
MSG_TS_DEL        = 'Delete task number: '
MSG_TS_DEL_ALL    = "Really delete all tasks? (y/n)"
MSG_TS_MOVE       = 'Move task from number: '
MSG_TS_MOVE_TO    = 'Move task to number: '
MSG_TS_EDIT       = 'Edit task number: '
MSG_TS_TOG        = 'Toggle subtask number: '
MSG_TS_SUB        = 'Add subtask for task number: '
MSG_TS_TITLE      = 'Enter subtask: '
MSG_TS_IM         = "Import tasks from Calcurse? (y/n)"
MSG_TS_TW         = "Import tasks from Taskwarrior? (y/n)"
MSG_TS_NOTHING    = "Nothing planned..."
MSG_TS_PRIVACY    = "Toggle privacy of task number: "

CALENDAR_HINT     = "Space · Switch to journal   a · Add event  n/p · Change month   ? · All keybindings"
CALENDAR_HINT_D   = "Space · Switch to journal   a · Add event  n/p · Change day   ? · All keybindings"
JOURNAL_HINT      = "Space · Switch to calendar   a · Add task   v · Done   i · Important   ? · All keybindings"

ERR_FILE1 = "Looks like there is a problem in your config.ini file.Perhaps you edited it and entered a wrong line."
ERR_FILE2 = "Try removing your config.ini file and run the program again, it will create a fresh working config file."

DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
DAYS_PERSIAN = ["SHANBEH", "YEKSHANBEH", "DOSHANBEH", "SESHANBEH", "CHAHARSHANBEH", "PANJSHANBEH", "JOMEH"]

MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
MONTHS_PERSIAN = ["FARVARDIN", "ORDIBEHESHT", "KHORDAD", "TIR", "MORDAD", "SHAHRIVAR", "MEHR", "ABAN", "AZAR", "DEY", "BAHMAN", "ESFAND"]