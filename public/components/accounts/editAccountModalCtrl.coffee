angular.module("buckit").controller 'editAccountModalCtrl', [
  "$scope"
  "$modalInstance"
  "Accounts"
  "accountId"
  ($scope, $modalInstance, Accounts, accountId) ->

    $scope.accountTypes = [
      "liability"
      "asset"
      "income"
      "expense"
      "equity"
    ]

    if accountId
      $scope.isNewAccount = false
      Accounts.get({id: accountId}).$promise.then (account) ->
        $scope.account = angular.copy(account)
      , (error) ->
        alert error
    else
      $scope.isNewAccount = true
      $scope.account =
        name: null
        type: "asset"

    $scope.save = ->
      f = if $scope.account.id then Accounts.update else Accounts.save
      f($scope.account).$promise.then (account) ->
        $modalInstance.close account
      , (response) ->
        alert "Error saving!"

    $scope.cancel = ->
      $modalInstance.dismiss 'cancel'

]
