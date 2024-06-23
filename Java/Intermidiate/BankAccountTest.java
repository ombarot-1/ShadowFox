import org.junit.jupiter.api.*;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

public class BankAccountTest {

    private BankAccount bc;

    @BeforeEach
    void setup(){
        bc = new BankAccount(007, 1000);
    }

    @Test
    void testInitialBalance(){
        assertEquals(1000, bc.getBalance());
    }

    @Test
    void testdepositNegetiv(){
        bc.deposit(-1000);
        List<String> his = bc.getTransactionHistory();
        assertFalse(his.contains("Amount deposit:-1000.0"));
    }

    @Test
    void testwithdrawNegetiv(){
        bc.withdraw(-1000);
        List<String> his = bc.getTransactionHistory();
        assertFalse(his.contains("Amount withdraw:-1000.0"));
    }

    @Test
    void testwithdrawOveramont(){
        bc.withdraw(5000);
        List<String> his = bc.getTransactionHistory();
        assertFalse(his.contains("Amount withdraw:5000.0"));
    }

    @Test
    void testTransactionHistory() {
        bc.deposit(5000);
        bc.withdraw(2000.0);
        List<String> history = bc.getTransactionHistory();
        assertEquals(3, history.size());
        assertTrue(history.contains("Initial Balance:1000.0"));
        assertTrue(history.contains("Amount deposit:5000.0"));
        assertTrue(history.contains("Amount withdraw:2000.0"));
    }






    



    
}
