# Welcome to the Database Tracker! Let's start by introducing ourselves (Part A), calculating discount amount and discounted price for a product on sale (Part B), and then fixing the bugs for a popular nursery rhyme! (Part C)

# Here is our main method for our program, where Python starts reading our code and executing commands indented inside the main method!
if __name__ == "__main__":
  
  ## Part A ##
  # TODO String: assign a variable called (name) to your name
  
  # TODO Integer: assign a variable called (grade) to your grade level
  
  # TODO Float: assign a variable called (weeks) to the value 5.0
  
  print("Introducing Myself\n")
  
  # Here you are introducing yourself with a print statement using concatenation with a (+) sign to connect strings, integers, and floats together
  # Note that the variables (grade) and (weeks) are enclosed in str(). We use str() to typecast integers and floats to a string data type. This is crucial so that the computer can interpret your information and execute this print statement.
  print("Hello everyone! My name is " + name + " and I am in " + str(grade) + "th grade. I am a Data Programming student in the " + str(weeks) + " weeks long Explorer Program!")
  
  ## Part B ##
  print("\nCalculating Discount for a Product on Sale\n")
  
  # Price of Product 
  price = 1.30
  
  print("Price of Product: ", price)
  
  # Discount Percentage
  discount_percentage = 50.0 
  
  print("Discount Percentage: ", discount_percentage)
  
  # Discount Amount
  discount_amount = 0
  
  print("Discount Amount: ", discount_amount)
  
  # Discounted Price
  discounted_price = 0
  
  print("Discounted Price: ", discounted_price)
  
  # Formulas to Calculate Price for a Product on Sale
  # Discount Amount = (Discount Percentage x Price)/100
  # Discounted Price = Price - Discount Amount
  
  # TODO Replace the formula with the variables initialized above and assign to variables called (discount_amount) and (discounted_price)
  
  
  
  # TODO Use print statements to print out the discount amount and the discounted price
  
  
  
  ## Part C ##
  q = # TODO Replace this comment with the escape sequence for a quote
  
  # Use your knowledge of escape sequences to fix the bugs (errors) that occur when this code segment is run
  # TODO Add the variable (q) to places where there are quotation marks in this nursery rhyme (check original nursery rhyme in comments below) to print quotation marks without errors in the code!
  
  print("\nTry reading aloud the Betty Botter Rhyme!\n")
  print("Betty Botter bought a bit of butter;")
  print("But," she said, "this butter’s bitter!")
  print("If I put it in my batter")
  print("It will make my batter bitter.")
  print("But a bit o' better butter")
  print("Will make my batter better.")
  
# Betty Botter Rhyme

# Betty Botter bought a bit of butter;
# “But,” she said, “this butter’s bitter!
# If I put it in my batter
# It will make my batter bitter.
# But a bit o’ better butter
# Will make my batter better.”
