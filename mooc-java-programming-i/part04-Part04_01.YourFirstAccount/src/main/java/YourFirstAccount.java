
public class YourFirstAccount {

    public static void main(String[] args) {
        // Do not touch the code in Account.java
        // Write your program here
        Account anonAccount = new Account("Anon", 100.0);

        anonAccount.deposit(20.0);
        System.out.println(anonAccount);
    }
}
