      String input;

      Scanner scanner = new Scanner(input);
      String res = new String();
      int sum = 0;
      Map<String, Integer> names = new HashMap<>();
      names.put("one",1);
      names.put("two",2);
      names.put("three",3);
      names.put("four",4);
      names.put("five",5);
      names.put("six",6);
      names.put("seven",7);
      names.put("eight",8);
      names.put("nine",9);


      while (scanner.hasNextLine()) {
          String line = scanner.nextLine();
          int one = -1;
          int two = -1;

          for (int i = 0; i < line.length(); ) {
              if (Character.isDigit(line.charAt(i))) {
                  if (one < 0) {
                      one = Integer.parseInt(String.valueOf(line.charAt(i)));
                      two = one;
                  } else {
                      two = Integer.parseInt(String.valueOf(line.charAt(i)));
                  }
                  ++i;
              } else {
                  var substr = line.substring(i);

                  int delta = 1;
                  for (var item: names.entrySet()) {
                      if (substr.startsWith(item.getKey())) {
                          int digit = item.getValue();

                          if (one < 0) {
                              one = digit;
                              two = one;
                          } else {
                              two = digit;
                          }

                          delta = 1;

                          break;
                      }
                  }

                  i += delta;
              }
          }

          int val = one * 10 + two;

          res += val + ",";
          sum += val;
      }

      System.out.println(sum);
