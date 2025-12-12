
radius_1 = float ( input ( ' Enter the radius of circle 1 : ' ) )
radius_2 = float ( input ( ' Enter the radius of circle 2 : ' ) )
radius_3 = float ( input ( ' Enter the radius of circle 3 : ' ) )
Pi = 3.14
area_1 = Pi * radius_1 * radius_1
area_2 = Pi * radius_2 * radius_2
area_3 = Pi * radius_3 * radius_3
area = { 'radius' : [ radius_1 , radius_2 , radius_3 ] , 'area' : [ area_1 , area_2 , area_3 ] }
print ( ' the areas of the circles are : ' , area [ 'area' ]    )
