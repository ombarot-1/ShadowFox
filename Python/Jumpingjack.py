Tareget = 100
Set = 10
total = 0

while total < Tareget:
    print(f'You completed {Set} jumping jack.')
    total += Set

    if total == Tareget:
        print('Congratulations!You completed the workout')
        break

    try:
        tired = input('Are you tired?(yes/y or no/n):').strip().lower()
        if tired not in ['yes','y','no','n']:
            raise ValueError('Error:Enter only valid values!')

        if tired in ['yes','y']:
            skip = input('You want to skip the remaining sets?(yes/y or no/n):').strip().lower()
            if skip not in ['yes','y','no','n']:
                raise ValueError('Error:Enter only valid values!')

            if skip in ['yes','y']:
                print(f'You completed a total of {total} jumping jacks."')
                break

            else:
                Remaining = Tareget - total
                print(f'{Remaining} jumping jacks are remaining.')

        else:
            Remaining = Tareget - total
            print(f'{Remaining} jumping jacks are remaining.')

    except ValueError as e:
        print(e)
        break

