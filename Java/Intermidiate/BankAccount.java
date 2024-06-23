import java.util.*;

public class BankAccount {
    private int AccountNumber;
    private double balance;
    private List<String> transactionHistory;

    public BankAccount(int AccountNumber,double InitialBalance){
        this.AccountNumber = AccountNumber;
        this.balance = InitialBalance;
        this.transactionHistory = new ArrayList<>();
        transactionHistory.add("Initial Balance:" + InitialBalance);
    }

    public int getAccountNumber(){
        return AccountNumber;
    }

    public double getBalance(){
        return balance;
    }

    public void deposit(double amount){
        if(amount > 0){
            balance += amount;
            transactionHistory.add("Amount deposit:" + amount);
        }
    }

    public void withdraw(double amount){
        if(amount > 0 && amount <= balance){
            balance -= amount;
            transactionHistory.add("Amount withdraw:" + amount);
        }
    }

    public List<String> getTransactionHistory() {
        return new ArrayList<>(transactionHistory);
    }
     
}