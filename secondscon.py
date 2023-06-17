###convertion of seconds in hours
total_seconds=int(input("please enter the no.of.seconds you wish to convert:"))
hours=total_seconds//3600
secs_still_remaining=total_seconds%3600
minutes=secs_still_remaining//60
secs_finally_remaining=secs_still_remaining%60
print("Hours=",hours,"Minutes=",minutes,"Seconds=",secs_finally_remaining)
















