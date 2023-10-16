# easy-money

A simple but powerful tool for budgeting and tracking finances.

Not *actually* released yet.

# Quickstart

The easiest way to start using easy-money is to use [pipx](https://pypa.github.io/pipx/installation/)

    pipx install candid_cash
    easy-money

Yes - you have to install `candid_cash`, even though this is called Easy Money.
Don't worry about it. [Unless you want to](https://pypi.org/help/#project-name).


By default you'll be presented with a text UI that shows you a summary of your
current everything:

    $0 free, $0 in 0 goals (0 over time, 100% funded)
    Type "help" for help.
    > 

By default currency is $/USD, but you can change that. This summary will also
be printed before every prompt, which can also be changed.

You can add money (normally you'd do this when you get money, like on payday or
when someone hands you a stack of $100 bills).

    > add 100
    $100 free, $0 in 0 goals (0 over time, 100% funded)

Now you can create some goals and add the money to your goals:

    > new goal Gas
    Gas - $0> move 50
    $50 free, $50 in 1 goals (0 over time, 100% funded)
    Gas - $50> exit
    $50 free, $50 in 1 goal (0 over time, 100% funded)
    > new goal Eating out
    Eating out - $0> move 25
    $25 free, $75 in 2 goals (0 over time, 100% funded)
    Eating out - $25> exit
    > new goal Groceries
    Groceries - $0> move 50
    OOPS! Only $25 available. Try move 25 (or less)
    Groceries - $0> move 25
    $0 free, $100 in 3 goals (0 over time, 100% funded)
    Groceries - $25> exit
    > new goal New computer
    New computer - $0> add 20
    $0 free, $120 in 4 goals (0 over time, 100% funded)
    New computer - $20> exit
    $0 free, $120 in 4 goals (0 over time, 100% funded)
    > new target
    Goal name: Birthday
    Would you like to save per (t)ime or for a (d)ate? d
    What date? 2024-06-25
    Total amount? 28
    That will be $0.11 per day over 254 days.
    $0 free, $120 in 4 goals ($28 over time, 0% funded)
    > add 14
    $14 free, $120 in 4 goals ($28 over time, 0% funded)
    > move 14 to Birthday
    $0 free, $120 in 4 goals ($28 over time, 50% funded)
    > new target
    Goal name: New car
    Would you like to save per (t)ime or for a (d)ate? t
    How often - (D)aily, (W)eekly, (B)i-weekly, (M)onthly? D
    How much per day? 0.25
    How much total? 25,000
    You will reach $25,000 saved on 2297-06-30
    $0 free, $120 in 4 goals ($14/25,028 over time, 0% funded)
    >

You may already know this, but Easy Money is based on the [envelope
method](https://en.wikipedia.org/wiki/Envelope_system) method of budgeting.
But, better. Maybe!

For more help on how to use EM, type help at the prompt(s).

# Deeper Dive

When writing Easy Money, I heavily borrowed from Simple. For me, it was a
life-changing use of technology and made it fun to see how long it would take
to save up for things, or where I was really spending my money. It helped me to
decide if I really wanted to buy something, or if I was better off doing
something else. However, PNC bank bought out Simple, and pretty much ruined my
life. For several years I've tried a multitude of different approaches, but
none of them have worked very well. Even EM may not work so well for me, but
the goal is to make it almost as easy to use as Simple was. But licensed AGPL,
which is the most aggressive Copyleft license I'm aware of.

To put it bluntly, the goal of EM is to allow you to take control of your
financial situation, regardless of the whims of a corporation. At any point,
you may take EM and manage it yourself.


## Goals and Funding Schedules

Goals are the envelopes of the envelope method. And there are two types of
goals - immediate, and over time. For an immediate goal it's like taking cash
and putting it directly into an envelope. For an over time goal it's something
that you'd like to save up for. Maybe you want a new video game console, a new
outfit, or need to repair your car. You probably need to buy new tires in a few
years. You'll certainly need to change your oil.

For something like oil you know that it's probably 3 months - and around here a
full synthetic oil change is about $80 right now. So that would be about $0.89
for a daily funding schedule. Or about $6.25 per week. Or $12.50 bi-weekly. Or
$27 monthly. But you don't need to remember that or figure it out. That's where
Easy Money makes life easier for you. EM will track all of that for you. You
just have to input when you get and spend money - just like when you would put
money into or take money out of your envelopes.

## Free Money!

Well, not free as in without cost, but free as in unallocated. If your money
isn't allocated to a particular goal, it's considered free money. That is,
spend it on whatever you want! Or keep it as an emergency fund and only spend
from your goals. Do what you want, I'm not your dad. Except for the 5 of you
for whom I am your dad. But you're probably an adult by the time you're using
this so you can use it however you want.

But, in order to fund a goal you have to have some free money. You can't just
make up money, despite all of this stuff being made up anyway. You're the one
who decides what the numbers mean.

## Imports

If you're like me, you hate actually inputting the transactions that you make -
even if it's easy! Like, uuuugh. It's the worst. So Easy Money offers an
importer. When you import transactions into EM, your bank or CC should offer
.csv downloads. You can import these into EM. If you're like me there's also a
non-zero chance that you'll end out re-importing the same transactions. In my
case I've had a in-the-middle-of-a-billing-cycle file, or monthly files, and
then I pulled in a yearly file. Whoops! Don't worry - if you notice that you've
got duplicate entries, we retain the batch/filename information from when they
were imported, so you can easily just delete the whole batch.

## Reports

There ~are currently only~ will soon be a couple of basic reports offered:

- Monthly in/out - how much money came in this month and how much went out? (By
  calendar month as well as last 30 days)
- Yearly in/out - good for tracking your long-term monetary goals.
- Runway - Based on your current reserves, given your recent spending, how long
  until you're out of cash? It's a sucky thing to consider, but it's better
  than not knowing.


# Roadmap

These are things that we want to do:

- Implement basic behavior as documented here in the README
- Create installer/upload to pypi
- Add importer
- Add some reporting


# Changelog

We use [keepachangelog](https://keepachangelog.com/). We also use [CalVer](https://calver.org/) for
versioning. Specifically YY.MM.patch.

## Unreleased

- Anything!
