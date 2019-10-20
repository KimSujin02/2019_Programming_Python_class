# decimal - 10진수
# octabal - 8진수
# binary - 2진수
f = open("data.bin","wb")       #bin로 하는거  갱장히 중요 !
byte_arr = bytes([255,0,127])   #3개를 저장했으니까 3byte
f.write(byte_arr)
f.close()

