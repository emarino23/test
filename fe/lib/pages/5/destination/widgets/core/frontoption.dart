import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';

class DestinationFrontOptionWidget extends StatelessWidget {
  const DestinationFrontOptionWidget(
      {Key? key,
      this.destination = "coast",
      required this.index,
      required this.type,
      this.isListed = false})
      : super(key: key);

  final String destination;
  final index;
  final type;
  final isListed;
  @override
  Widget build(BuildContext context) {
    // ignore: unnecessary_null_comparison

    return Obx(() {
      var t = arrivalDate.value;
      var dest = Rx(getDestinationValueByName(destination));
      if (dest.value.isNotEmpty) {
        return Stack(children: [
          Padding(
            padding: EdgeInsets.only(
              top: Get.height * 0.04,
              left: Get.width * 0.00,
            ),
            child: Image.asset(
              "assets/images/" + dest.value["data"][2],
              // width: Get.width * 0.5, height: Get.height * 0.2
            ),
          ),
          Padding(
            padding: EdgeInsets.only(
              top: Get.height * 0.07,
              left: Get.width * 0.0,
            ),
            child: Align(
              alignment: Alignment.centerLeft,
              child: Image.asset("assets/images/" + dest.value["data"][3],
                  width: Get.width * 0.4, height: Get.height * 0.1),
            ),
          ),
          Row(
            children: [
              if (type == "arrival")
                Padding(
                  padding: EdgeInsets.only(
                    top: Get.height * 0.01,
                    left: Get.width * 0.0,
                  ),
                  child: Row(
                    children: [
                      Text("Arrival",
                          style: KTextSytle(
                                  context: context,
                                  fontSize: 12,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white)
                              .getStyle()),
                      SizedBox(width: Get.width * 0.2),
                      Image.asset("assets/images/1x/arrival.png",
                          color: Colors.yellowAccent,
                          width: Get.width * 0.05,
                          height: Get.height * 0.1),
                    ],
                  ),
                ),
              if (type == "departure")
                Padding(
                  padding: EdgeInsets.only(
                    top: Get.height * 0.01,
                    left: Get.width * 0.0,
                  ),
                  child: Row(
                    children: [
                      Text("Departure",
                          style: KTextSytle(
                                  context: context,
                                  fontSize: 12,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white)
                              .getStyle()),
                      SizedBox(width: Get.width * 0.2),
                      Image.asset("assets/images/1x/departure.png",
                          color: Colors.redAccent,
                          width: Get.width * 0.05,
                          height: Get.height * 0.1),
                    ],
                  ),
                ),
            ],
          ),
          Obx(() {
            var t = arrivalDate.value;
            if (isListed ||
                !validateDragDestinationOptions(destination, index, type)
                    .value) {
              return Padding(
                padding: EdgeInsets.only(
                  top: Get.height * 0.04,
                  left: Get.width * 0.00,
                ),
                child: Image.asset(
                  "assets/images/" + dest.value["data"][2],
                  color: Color.fromARGB(100, 10, 10, 10),
                  // width: Get.width * 0.4,
                  // height: Get.height * 0.2
                ),
              );
            } else {
              return Text('');
            }
          }),
        ]);
      } else {
        return Text("");
      }
    });
  }
}
