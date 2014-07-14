window.TransactionCtrl = ($scope, ReconciledStatus, Account, Payee) ->

  $scope.reconciled_statuses = ReconciledStatus.all()
  $scope.accounts = Account.query()
  $scope.payees = Payee.query()

  $scope.account_split = (s for s in $scope.transaction.splits \
    when s.account_id == $scope.account.id)[0]

  non_account_splits = (s for s in $scope.transaction.splits \
    when s.account_id != $scope.account.id)

  if non_account_splits.length > 1
    $scope.displayCategory = 'Splits'
  else
    split = non_account_splits[0]
    Account.get {account_id: split.account_id}, (account) ->
      $scope.displayCategory = account.name

  $scope.edit = () ->
    $scope.editing = true
    $scope.newTransaction = $.extend true, {}, $scope.transaction

  $scope.addSplit = () ->
    $scope.newTransaction.splits.push
      id: null
      transaction_id: $scope.newTransaction.id
      account_id: null
      amount: 0
      reconciled_status: 'not_reconciled'

  $scope.ok = () ->
    $scope.editing = false
    console.log $scope.newTransaction

  $scope.cancel = () ->
    $scope.editing = false
