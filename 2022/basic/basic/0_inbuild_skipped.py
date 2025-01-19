# eval
# exec
# repr


# # What is Python Collections Module
# from collections import Counter,defaultdict,OrderedDict,namedtuple
# issubclass(Counter,dict) and issubclass(defaultdict,dict) and issubclass(OrderedDict,dict)



# We can also perform some operations on a date object:

# d=datetime.date(2018,12,30)
#  td=datetime.timedelta(0,99999)
# d1=d+td
# d1
# d1<d
# Python time Objects
# t=datetime.time(11,59,59,99999)
# date.ctime()
# date.__str__()

# strftime()
# Now what if you wanted to display the Python date and time in the format you wish to? The strftime() method takes a format and optionally, a Python time tuple, and returns the date in the format you specify. The syntax is as follows.
# Time.strftime(format[, t])
# You can apply the following directives in the format, as per your need.
# %a – abbreviated day of week
# %A – full day of week
# %b – abbreviated name of month
# %B – full name of month
# %c – preferred date and time representation
# %C – century number (the year divided by 100; range 00 to 99)
# %d – day of month (1 to 31)
# %D – the same as %m/%d/%y
# %e – day of month (1 to 31)
# %g – like %G, but without the century
# %G – 4-digit year corresponding to the ISO week number (ref. %V).
# %h – same as %b
# %H – hour; using a 24-hr clock (0 to 23)
# %I – hour; using a 12-hr clock (1 to 12)
# %j – day of year (1 to 366)
# %m – month (1 to 12)
# %M – minute
# %n – newline character
# %p – AM/PM according to given time value
# %r – time in AM/PM representation
# %R – time in 24-hr representation
# %S – second
# %t – tab
# %T – current time; equal to %H:%M:%S
# %u – day of week as a number (1 to 7); Monday=1
# %U – week of year, beginning with the first Sunday as the first day of the first week
# %V – The ISO 8601 week of year (1 to 53); week 1 is the first with at least 4 days in the current year, and with Monday as the first day of the week
# %W – week of year; beginning with the first Monday as the first day of the first week
# %w – day of week as a decimal; Sunday=0
# %x – the preferred date representation without the time
# %X – the preferred time representation without the date
# %y – year without century (00 to 99)
# %Y – year including century
# %Z or %z – time zone/name/abbreviation
# %% – a % character
# Let’s try printing the shortened name of the month in the local time in Python.
# >>> time.strftime("%b",time.localtime())
# Let’s try another one.
# >>> time.strftime("%B %uth, '%y",time.localtime())

