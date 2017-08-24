# @ 2014.12.16

'''--------------------------------
    First Edition

    by: Haiyang Huang
------------------------------------'''
print " ======     Aschaffenburg     ====== "
print ("      11D supermarket system          ")
print ("          Test version                ")
print " ===================================\n"

first = raw_input(" How many persons: ");  # return number to 1st var.

# Type in Not alphabet
if ( True == first.isalpha() ):            
    print (" Please input a number and re-start. ")

else:
    num = int(first)
    #-------------------------------------------------------------
    if ( num > 1 and num < 10 ):
        print  "\n This time have %d persons in total." %(num)
        print  "----------------------------------------\n"

        '''--------------------------
          input the names of person
        -----------------------------'''
        i = num;
        a_name  = []
        a_money = []

        while i>0:
            t = raw_input(" Please enter the names:  ");
            m = input(" Please enter the money he paid:  ");
            a_name.append(t);
            a_money.append(m);
            i = i-1;
            
        print "\n ====== Those are the results ====== \n"
        print " Peoples are %s \n" %(a_name)
        print " corresponding amount is: %s " %(a_money)

        '''
          calculation
        '''
        j = num-1;
        total = 0.0;

        while j>=0:
            total = total + a_money[j]
            j = j-1;

        aver = total/num;

        print "\n ====== individule detail  ====== \n"
        print " The total number is  : %10.3f Euro \n" %(total)
        print " The average amount is: %10.3f Euro \n" %(aver)

        '''
          final pay out
        '''
        k = num-1;
        fi_mo = a_money;

        while k >= 0:
            fi_mo[k] = a_money[k]- aver;    
            k = k-1
        #---------------------------------------
        j = num-1;
        i = 0;
        while i<=j:
            print " %15s : %10.3f Euro  " %(a_name[i],fi_mo[i])
            i = i+1;
        print  " ----------------------------------------"
        print  " ----------------------------------------\n"
    #------------------------------------------------------------ 
    elif num <= 1:
        print (" Please enter a valid number and re-start. ")

    else:
        print (" number out of limited range,please restart. ")
    
    
#------ End ------------------
raw_input("Please<Enter>:")
