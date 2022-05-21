          #   """sep method"""
print('s','h','n',sep='@')#s@h@n
print('s','h','n',sep='@' "n")#s@nh@nn@n
print('s','h','n',sep='@' +'n')#s@nh@nn@n
print('s','h','n',sep='@''ok')#s@okh@0kn@ok
print('s','h','n',sep='@ok')#s@okh@okn@ok
print('s','h','n',sep='_@')#s_@h_@n_@
"""end method"""
print('s','h','n',end='@' "n")#s h n@ns h n@ns h n@oks h n @oks h n_@
print('s','h','n',end='@' +'n')
print('s','h','n',end='@''ok')
print('s','h','n',end='@ok')
print('s','h','n',end='_@')

print('s','h','n',end='@')#s h n@s h n@ns h n@ns@okh@okn
print('s','h','n',end='@' "n")#s@okh@okn  #s_@h_@n
print('s','h','n',end='@' +'n')
print('s','h','n',sep='@''ok')
print('s','h','n',sep='@ok')
print('s','h','n',sep='_@')

print('s','h','n',end='@')#s h n@s h n@ns h n@ns h n@oks h n@oks h n
print('s','h','n',end='@' "n")
print('s','h','n',end='@' +'n')
print('s','h','n',end='@''ok')
print('s','h','n',end='@ok')
print('s','h','n',end='')

#           '''end&\nsep'''
print('s','h','n',end='@\n')             #s h n@n
                                        #   s h n@n
                                        #   s@ok
                                        #   h@ok
                                        #   n
                                        #   s@ok
                                        #   h@ok
                                        #   n
                                        #   s_@
                                        #   h_@
                                        #   n

print('s','h','n',end='@' "n\n")
print('s','h','n',end='@' +'n\n')
print('s','h','n',sep='@''ok\n')
print('s','h','n',sep='@ok\n')
print('s','h','n',sep='_@\n')

print('s','h','n\n',end='@')#s h n
                                #    @s h n
                                #    @ns h n
                                #    @ns@okh@okn

                                #    s@okh@okn

print('s','h','n\n',end='@' "n")#s_@h_@n # 
print('s','h','n\n',end='@' +'n')
print('s','h','n\n',sep='@''ok')
print('s','h','n\n',sep='@ok')
print('s','h','n\n',sep='_@')
 
print('s','h','n\n',end='@')                    #s h n
print('s','h','n\n',end='@' "n")                #@s h n
print('s','h','n\n',end='@' +'n')                #@ns@okh@okn
print('s','h','n\n',sep='@''ok',end='')           #s@okh@okn
print('s','h','n\n',sep='@ok',end="")              #s_@h_@n
print('s','h','n\n',sep='_@',end='')



            # """sep &end """
print('s','h','n', sep="e\n",end='@')   #se
                                         #he
                                         #n@sehen@
print('s','h','n', sep="e",end='@')        #sehen@n
print('\ns','h','n',sep="e",end='@' "n")   #sehen@n
print('\ns','h','n',sep="e",end='@' +'n') #sehen@ok
print('\ns','h','n',sep="e",end='@''ok')#sehen@ok
print('\ns','h','n',sep="e",end='@ok')#sehen .
print('\ns','h','n',sep="e",end=' .')

              #'''end&sep'''
print('s','h','n', end="e\n",sep='@')            #s@h@ne
print('s','h','n', end="e",sep='@')           #s@h@ne
print('\ns','h','n',end="e",sep='@' "n")      #s@nh@nne
print('\ns','h','n',end="e",sep='@' +'n')     #s@nh@nne
print('\ns','h','n',end="e",sep='@''ok')  #s@okh@okne
print('\ns','h','n',end="e",sep='@ok')   #s@okh@okne
print('\ns','h','n',end="e",sep='.')     #s.h.neshnshnshnshn
                                               #shn
                                               #shn
                                               #
print('shn'*3,end='')                     #shn
print('shn\n'*3,end='')                    #shn
print(' \nshn'*3,end='')                #shnshnshnshn
print('shn'*3,end='')
