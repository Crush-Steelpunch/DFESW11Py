from cli_badges import badge

failedBadge = badge("failed",'2',messagebg='red')
skippedBadge = badge('skipped', '1', messagebg='yellow',messagecolor='black')
successBadge = badge('success','8', messagebg='green',messagecolor='black')

print(failedBadge, successBadge, skippedBadge)