import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'customdescription.dart';
import 'customformexperiencedetail.dart';
import 'customformtitle.dart';

class CustomFormDayWidget extends StatelessWidget {
  const CustomFormDayWidget({
    Key? key,
    required this.indexes,
  }) : super(key: key);

  final List<int> indexes;
  @override
  Widget build(BuildContext context) {
    try {
      int destIndex = indexes[0];
      int dayIndex = indexes[1];
      var tour = globalctx.memory["tour"];
      var destinations = tour["destinations"];
      var destination;
      try {
        destination = destinations[destIndex.toString()];
      } catch (e) {
        destination = destinations[destIndex];
      }
      var daysData = destination["daysData"] ?? {};
      var days = daysData.entries.toList();
      var day = days[dayIndex];
      var daydescription = day.value['day_description'] ?? '';
      int destIndexPlusDayIndex = destIndex + dayIndex;
      var destIndexAccumulated = destIndex * (destIndex + 1) / 2;
      Object dayLabelIndex =
          (destIndexPlusDayIndex + destIndexAccumulated).round();

      var destSize = 0;
      for (var e in destinations) {
        destSize += parseInt(e["explorationDay"]);
      }
      var label = dayLabelIndex == 0
          ? "Arrival"
          : dayLabelIndex == destSize - 1
              ? "Departure"
              : "$dayLabelIndex#####";
      var dayLabel = label;
      var actualcost = 0.obs;
      var cost = getFormValue(globalctx.memory, "netRate", destIndex, 0);
      actualcost.value = cost + 217 * 2;
      totalNetRate.value += actualcost.value;
      return Column(
        children: [
          CustomFormTitleWidget(level: 4, label: "Day: $dayLabel#####"),
          CustomDescriptionWidget(
              text: daydescription, width: 0.55, fontSize: 10),
          CustomFormExperiencesDetailWidget(indexes: indexes),
          CustomDescriptionWidget(
              fontWeight: FontWeight.bold,
              text: "Transfer per day: \$217",
              width: 0.55,
              fontSize: 10),
          CustomDescriptionWidget(
              fontWeight: FontWeight.bold,
              text: "Guide Service per day: \$217",
              width: 0.55,
              fontSize: 10),
          Wrap(
            children: [
              CustomDescriptionWidget(
                text: "Day Net Rate: ",
                width: 0.35,
                fontSize: 12,
                fontWeight: FontWeight.bold,
              ),
              Obx(() {
                return CustomDescriptionWidget(
                  text: "\$ $actualcost",
                  width: 0.22,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                );
              }),
            ],
          ),
          SizedBox(height: Get.height * 0.01),
        ],
      );
    } catch (e) {
      return Text("ERROR: CustomFormDayWidget: $e");
    }
  }
}
