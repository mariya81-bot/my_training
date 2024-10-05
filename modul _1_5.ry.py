immutable_tuple_=1,2,3,'true','string'
print(immutable_tuple_)
immutable_tuple_[0]=200
print(immutable_tuple_)
immutable_tuple_1=([1,2],3)
immutable_tuple_1[0][0]=2
print(immutable_tuple_1)
mutable_list=["food",1,2,3]
mutable_list[0] = 3
print(mutable_list)