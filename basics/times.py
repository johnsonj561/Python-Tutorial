import time;

print '\n'

timeSinceEpoch = time.time()
print 'Time Since Epoch: ' + str(timeSinceEpoch)

localTime = time.localtime(timeSinceEpoch)
print 'Local Time: ' + str(localTime)

formattedTime = time.asctime(localTime)
print 'Formatted Time ' + str(formattedTime)

print '\n'
