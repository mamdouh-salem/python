radius_1 = float ( input ( ' Enter the radius of the first circle : ' ) )
radius_2 = float ( input ( ' Enter the radius of the second circle : ' ) )
radius_3 = float ( input ( ' Enter the radius of the third circle : ' ))
area_1 = 3.14 * radius_1**2
area_2 = 3.14 * radius_2**2 
area_3 = 3.14 * radius_3**2
list_of_areas = [ area_1 , area_2 , area_3 ]
print ( ' The areas of the circles are : ' , list_of_areas )
print ( " the area of the first and second circle are : " , list_of_areas [ 0 : 3 ] )
print ( " the area of the second and third circle are : " , list_of_areas [ 1 : 4 ] )
print ( " the area of the first and third circle are : " , list_of_areas [ 0 : 1 ] + list_of_areas [ 2 : 3 ] )

