import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

class KeypadWidget extends StatelessWidget {
  const KeypadWidget({
    Key? key,
    required this.experience,
  }) : super(key: key);

  final experience;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(left: Get.width * 0.3, top: Get.height * 0.0),
      child: Row(children: [
        TextButton(
          child: Text("Accept",
              style: KTextSytle(
                      context: context,
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: Colors.white)
                  .getStyle()),
          onPressed: () {
            if (leftHours[currentDay.value].value > 0) {
              promoteExperience("Leisure Time", "promoted");
            }
            Get.close(1);
          },
        ),
        TextButton(
          child: Text("Cancel",
              style: KTextSytle(
                      context: context,
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: Colors.white)
                  .getStyle()),
          onPressed: () {
            Get.close(1);
          },
        ),
      ]),
    );
  }
}