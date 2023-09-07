from django.db import models


class AuctionRoom(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # highest_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='won_auctions')

    def __str__(self):
        return self.name

class Bid(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(AuctionRoom, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bid {self.amount} in {self.room.name}"