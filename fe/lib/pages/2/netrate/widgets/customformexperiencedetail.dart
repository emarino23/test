import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'customdescription.dart';
import 'customformexperience.dart';

class CustomFormExperiencesDetailWidget extends StatelessWidget {
  const CustomFormExperiencesDetailWidget({
    Key? key,
    required this.indexes,
  }) : super(key: key);
  final List<int> indexes;
  @override
  Widget build(BuildContext context) {
    var destindex = indexes[0];
    var dayindex = indexes[1];
    var tour = globalctx.memory["tour"];
    var passengers = parseInt(tour["passengers"]);
    var destinations = tour["destinations"];
    var destination;
    try {
      destination = destinations[destindex.toString()];
    } catch (e) {
      destination = destinations[destindex];
    }

    var daysData = destination["daysData"];
    var days = daysData.entries.toList();
    var day = days[dayindex].value;
    var dayexps = day['experiences'];
    if (dayexps == null) {
      return Text("");
    }
    var expList = dayexps.keys.toList();
    var actualCost = 0;
    List<Widget> list = [];

    for (var i = 0; i < dayexps.length; i++) {
      var expName = expList[i];
      if (expName != "Leisure Time") {
        var expData = getExperienceDataByName(expName);
        int cost = expData.value["cost"];
        actualCost += cost * passengers;
        list.add(
            CustomFormExperienceRowWidget(indexes: [destindex, dayindex, i]));
      }
    }

    for (var room in destination.keys) {
      if (room.contains("hotelPax.")) {
        var roomKey = room.split(".")[1];
        var roomPax = parseInt(destination["hotelPax." + roomKey]);
        var roomData = filterCatalog("hotel", "description", roomKey)[0];
        var roomCost = parseInt(roomData["value"]["FITrate"]);
        actualCost += roomCost * roomPax;
        list.add(Wrap(
          children: [
            CustomDescriptionWidget(
              text: roomKey.toString().split("-")[1],
              width: 0.35,
              fontSize: 12,
              fontWeight: FontWeight.bold,
            ),
            CustomDescriptionWidget(
              text: "\$ $roomCost X $roomPax = \$ ${roomCost * roomPax}",
              width: 0.25,
              fontSize: 12,
              fontWeight: FontWeight.normal,
            ),
          ],
        ));
      }
    }

    setFormValue(globalctx.memory, "netRate", destindex, actualCost);
    return Padding(
      padding: EdgeInsets.only(left: Get.width * 0.05),
      child: Column(
        children: list,
      ),
    );
  }
}
