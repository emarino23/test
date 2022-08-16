import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'customdescription.dart';
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
    var tour = globalctx.memory["tour"];
    var destinations = tour["destinations"];
    var logistic = tour["logistic"];
    var promotedDestinationDay = destinations;
    var destindex = index;
    var destination;
    try {
      destination = promotedDestinationDay[destindex.toString()];
    } catch (e) {
      destination = promotedDestinationDay[destindex];
    }

    var explorationDay = (destination["explorationDay"]);
    var destName = destination["destination"].toString();
    var title = destName.replaceAll("_", " ").capitalize;
    var days = [].obs;
    Set dests = Set();
    for (var day = 0; day < explorationDay; day++) {
      var key = GlobalKey();

      globalctx.keys["day-$destindex-$day"] = key;
      if (!destName.toString().contains("cruise")) {
        daylist.add(Column(
          children: [
            CustomFormTitleWidget(level: 3, label: "$title"),
            CustomFormDayWidget(indexes: [destindex, day]),
          ],
        ));
      } else {
        days.add(day + 1);
        if (!dests.contains(title)) {
          dests.add(title);
          var cruiseData = filterCatalog(
              "cruises", "description", logistic["cruiseName"])[0];
          var cruiseCode = cruiseData["code"];
          var cabins = findCatalog("cabine");
          var cruiseCabins = cabins
              .where((element) =>
                  element["value"]["cruise_id"].toString() ==
                  cruiseCode.toString())
              .toList()
              .where((element) =>
                  element["value"]["days"].toString() ==
                  explorationDay.toString())
              .toList();
          var cabinsWidget = <Widget>[];
          for (var cabine in cruiseCabins) {
            cabinsWidget.add(
              CustomDescriptionWidget(
                  text:
                      "${cabine["description"]} Net Rate: \$ ${cabine["value"]["net_rate"]}",
                  width: 0.5,
                  fontSize: 12,
                  fontWeight: FontWeight.bold),
            );
          }
          daylist.add(Column(children: [
            Obx(() {
              return CustomFormTitleWidget(
                level: 1,
                label:
                    "$title ${logistic["cruiseName"]} ${days.length}D/${days.length - 1}N",
              );
            }),
            SizedBox(
                width: Get.width * 0.6,
                child: const Divider(color: Color.fromARGB(255, 0, 0, 0))),
            ...cabinsWidget,
            CustomDescriptionWidget(
                text: "Guide Service per day: \$217",
                width: 0.5,
                fontSize: 12,
                fontWeight: FontWeight.bold),
          ]));
        }
      }
    }

    return Column(
      children: daylist,
    );
  }
}
