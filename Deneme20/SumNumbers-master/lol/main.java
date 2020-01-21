public class MyMainClass {
  public static void main(String[] args) {
      Arrays.stream(args).forEach(System.out::println);
  }
}