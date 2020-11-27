def arithmetic_arranger(problems, StartPrint= False):

  # First condition: length of the problem (max 5)    
  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    arranged_problems= []
    top_space= ""
    end_space= ""
    body_space= ""
    dashes= ""

    for i, problem in enumerate(problems):
      n = problem.split()

  # Conditions: operator, only digits, four digits max
      if n[1] not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'."
      else:
        for digit in n[0]:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error: Numbers must only contain digits." 
          else: 
            continue

        for digit in n[2]:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error: Numbers must only contain digits." 
          else: 
            continue        
        if len(n[0]) > 4 or len(n[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'
        else:
          if n[1] == "+":
            sum_int = int(n[0]) + int(n[2])
          else:
            sum_int = int(n[0]) - int(n[2])
          
          length = max(len(n[0]), len(n[2])) + 2
          top_space += str(n[0].rjust(length))
          body_space += str(n[1] + n[2].rjust(length-1))
          dashes+= str("-" * length)
          end_space+= str(sum_int).rjust(length)

          if i < len(problems)-1:
            top_space += "    "
            body_space += "    "
            dashes += "    "
            end_space+= "    "
            
          if StartPrint == True: 
            arranged_problems = (top_space + "\n" + body_space + "\n" + dashes + "\n" + end_space)
          else: 
            arranged_problems = (top_space + "\n" + body_space + "\n" + dashes)


    return arranged_problems
