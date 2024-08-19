"""
Let’s say at Netflix we offer a subscription where customers can enroll for a 30-day free trial. After 30 days, customers will be 
automatically charged based on the package selected.

Let’s say we want to measure the success of acquiring new users through the free trial.

How can we measure acquisition success and what metrics can we use to measure the success of the free trial?

Source: Interview Query

Metrics
=======
What is Netflix’s business model?

1. Acquiring new users to their subscription plan.
2. Decreasing churn and increasing retention.

Now how does that affect how Netflix might acquire new users?

Think about the quality of acquisition, after signing up for paid memberships.

Can we measure the “effectiveness” of the acquisition in some way? In other words, what metrics can we measure that 
will define success on a top-level viewpoint for acquisition?

- One pretty simple example is the number of trial sign-ups divided by the number of leads. Leads can be defined by 
  customers that click on ads, sign up their email, or any other top of the funnel activity before the free trial sign-up. 

Let’s draw out a picture of the funnel:

Ads/Email/Commercial → Landing Page → Free Trial → Paid Membership

This metric will tell us the quality of the leads by acquisition channel at one part of the funnel. We can also segment 
this metric by the different acquisition channels and user demographics to see where it performs well (high conversion 
rate) and where it performs poorly (low conversion rate).

- Another metric that we can measure is the cost per free trial acquisition.

This is the cost for signing up each person to a free trial and can be calculated by the total marketing spend on 
advertising the free trial divided by the total number of free trial users.

 

Think you have a solution?

Have you considered long-term versus short-term engagement on the platform? 

How would that eventually affect how we value the free trial users?

Have you considered the amount of time spent on the app?

Could we segment this variable in some way that would be indicative of how likely they might be to convert once their free trial runs out?

What happens if we don’t have enough data to project out the lifetime value of the customer? Especially since thirty plus days is a long time to run an AB test to see if the free trial is worth it.



"""
from enum import Enum
from datetime import datetime


class Plan(Enum):
    BASIC = 1
    DELUXE = 2
    PREMIUM = 3


class Subscription:

    def __init__(self) -> None:
        self.email: str = None
        self.plan: Plan = None
        self.date: datetime = None
    
    def sign_up(self, email -> str, plan -> Plan) -> None:
        self.email = email
        self.plan = plan

    def cancel(self, date -> datetime):
        self.cancel_date = date
    
    def bill(self) -> int:
        