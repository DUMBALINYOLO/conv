from decimal import *
from django.db.models import Model
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from accounts.models import (
                        JournalEntry,
                        Account,
                        InterestBearingAccount,
                    )


from accounts.utils import (
                        format_currency,
                        format_percent
                    )
from accounts.permissions import LAAccountsClosingPermission
from accounts.serializers import (
                                InActiveAccountSerializer,
                                AccountCreateUpdateSerializer,
                                AccountListSerializer,
                                AccountDetailSerializer,
                                InterestBearingAccountCreateUpdateSerializer,
                                InterestBearingAccountListSerializer,
                                InterestBearingAccountDetailSerializer,
                            )



class InActiveAccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter(active='inactive').order_by('-id')

    serializer_class = AccountCreateUpdateSerializer


    # def get_serializer_class(self, *args, **kwargs):
    #     if self.action in ['create', 'put', 'update', 'patch']:
    #         return AccountCreateUpdateSerializer
    #     return AccountDetailSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter(active='active')

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['create', 'put', 'update', 'patch']:
            return AccountCreateUpdateSerializer
        return AccountDetailSerializer

    

    #may have to filter a queryset in future but for now this can server our purposes

class InterestBearingAccountViewSet(viewsets.ModelViewSet):
    queryset = InterestBearingAccount.objects.filter(active=True)
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['create', 'put']:
            return  InterestBearingAccountCreateUpdateSerializer
        elif self.action == 'retrieve':
            return InterestBearingAccountDetailSerializer
        return InterestBearingAccountListSerializer


