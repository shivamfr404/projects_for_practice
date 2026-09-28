def ordinalSuffix(number):
    if str(number).endswith(("11","12","13")):
        print(str(number)+"th")
ordinalSuffix(11)
ordinalSuffix(12)
ordinalSuffix(13)