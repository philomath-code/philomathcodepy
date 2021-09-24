#author: daniel medina
#date: 9.24.2021
import uuid
class random:
    #returns random guid without dashes
    def random_guid_hex(self):
        return uuid.uuid4().hex
    #returns random guid with dashes
    def random_guid(self):
        return uuid.uuid4()
