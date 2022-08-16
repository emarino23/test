import 'package:flutter/material.dart';
import 'package:get/get_utils/src/extensions/string_extensions.dart';
import 'package:naver_crs/index.dart';
import 'customformday.dart';
import 'customformtitle.dart';

class CustomFormDestination extends StatelessWidget {
  const CustomFormDestination({
    Key? key,
    required this.index,
    required this.destination,
  }) : super(key: key);

  final int index;
  final destination;
  @override
  Widget build(BuildContext context) {
    List<Widget> daylist = [];
    var promotedDestinationDay = globalctx.memory["destinations"];
    var destIndex = index;
    var destination = promotedDestinationDay[destIndex.toString()];
    var destName = destination["destination"];
    var explorationDay = parseInt(destination["explorationDay"]);
    var title = destination["destination"].toString().capitalize;
    var realAcc = 0;

    for (var i = 0; i < destIndex; i++) {
      var destination = promotedDestinationDay[i.toString()];
      var explorationDay = parseInt(destination["explorationDay"]);
      realAcc += explorationDay;
    }

    var starts = currentDayFormat.format(
        arrivalDate.value.add(Duration(days: destIndex == 0 ? 0 : realAcc)));
    var ends = currentDayFormat.format(
        arrivalDate.value.add(Duration(days: explorationDay + realAcc)));

    if (!destName.toString().contains("cruise")) {
      for (var day = 0; day < explorationDay; day++) {
        var key = GlobalKey();
        globalctx.keys["day-$destIndex-$day"] = key;
        daylist.add(Column(
          children: [
            RepaintBoundary(
                // key: globalctx.keys["day-$index-$day"],
                child: CustomFormTitleWidget(
                    level: 3,
                    label:
                        "$title ${explorationDay}${destIndex == 0 ? "N" : "D"}/${explorationDay - 1}${destIndex == 0 ? "D" : "N"}   $starts ${destIndex == globalctx.destinations.length - 1 ? "Departure" : ends}  ")),
            CustomFormDayWidget(indexes: [destIndex, day]),
          ],
        ));
      }
    } else {
      daylist.add(Column(
        children: [
          CustomFormTitleWidget(
              level: 3,
              label:
                  "${title.toString().replaceAll("_", " ").toString().capitalize!} ${globalctx.memory["logistic"]["cruiseName"]} ${explorationDay}D/${explorationDay - 1}N $starts $ends"),
        ],
      ));
    }

    return Column(
      children: daylist,
    );
  }
}
