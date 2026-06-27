subscribers={
    "a@gmail.com"
    "b@gmail.com"
    "c@gmail.com"
}

customers={
    "d@gmail.com"
    "e@gmail.com"
    "f@gmail.com"
}
never_purchased=subscribers-customers
purchased_not_subscribed=customers-subscribers

print("subscribers who never purchased:",never_purchased)
print("customers who purchased but not subscribed:",purchased_not_subscribed)