public class PalindromeChecker {
    public static boolean isPalindrome(String str) {
        String cleaned = str.replaceAll("\\s+", "").toLowerCase();
        int left = 0;
        int right = cleaned.length() - 1;

        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("Racecar")); // true
        System.out.println(isPalindrome("Hello"));   // false
    }
}

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class HTMLComplementaryColorTest {
  @Test
  public void emptyStringEqualTo000000() {
    assertEquals("#FFFFFF", HTMLComplementaryColor.getReversedColor(""));
  }
  @Test
  public void resultShouldBeginsWithHashChar() {
    assertEquals('#', HTMLComplementaryColor.getReversedColor("0").charAt(0));
  }
  @Test(expected=IllegalArgumentException.class)
  public void incorrectHexStringLength() {
    HTMLComplementaryColor.getReversedColor("1234567");
  }
  @Test(expected=IllegalArgumentException.class)
  public void invalidCharacterInHexColorShouldThrowError() {
    HTMLComplementaryColor.getReversedColor("AA00ZZ");
  }
  @Test(expected=IllegalArgumentException.class)
  public void hashCharInHexColorShouldThrowError() {
    HTMLComplementaryColor.getReversedColor("#AAFFAA");
  }
}

class Solution{

  public static long toggleBit(long n, long position){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
  
  public static long setBit (long n, long position){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
  
  public static long clearBit (long n, long position){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
  
  public static boolean isBitSet(long n, long position){
    //PUT YOUR LOVELY CODE HERE ^_^
    return false;
  }
  
  public static long setMultipleBits(long n, long mask){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
  
  public static long clearMultipleBits(long n, long mask){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
  
  public static long toggleMultipleBits(long n, long mask){
    //PUT YOUR LOVELY CODE HERE ^_^
    return -1;
  }
}

class SolutionTest {
  
    @Test
    void testSomething() {
        assertTrue(Kata.validateHello("hello"));
        assertTrue(Kata.validateHello("ciao bella!"));
        assertTrue(Kata.validateHello("salut"));
        assertTrue(Kata.validateHello("hallo, salut"));
        assertTrue(Kata.validateHello("hombre! Hola!"));
        assertTrue(Kata.validateHello("Hallo, wie geht\'s dir?"));
        assertTrue(Kata.validateHello("AHOJ!"));
        assertTrue(Kata.validateHello("czesc"));
        assertTrue(Kata.validateHello("Ahoj"));
        assertFalse(Kata.validateHello("meh"));
    }
}

public class Kata{
  public static boolean validateHello(String greetings){
    //Your code
    return false;
  }
  
}

int sum = 0;
for (int i = 1; i <= 5; i++) {
  sum = sum + i;
}
System.out.println("Sum is " + sum);
