def find_common_participants(group1, group2, rasd=','):
    participants1 = group1.split(rasd)
    participants2 = group2.split(rasd)

    common_participants = list(set(participants1) & set(participants2))
    common_participants.sort()

    return common_participants

group1 = "Алиса,Яна,Ваня"
group2 = "Яна,Руслан,Ваня"
common_participants = find_common_participants(group1, group2)
print(common_participants)

