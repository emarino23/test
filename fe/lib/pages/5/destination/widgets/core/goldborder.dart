import 'package:flutter/material.dart';
import 'package:get/get.dart';

class GoldBorderWidget extends StatelessWidget {
  const GoldBorderWidget({Key? key, required this.child}) : super(key: key);
  final Widget child;
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Padding(
          padding:
              EdgeInsets.only(top: Get.height * 0.04, left: Get.width * 0.0),
          child: Image.asset(
            "assets/images/1x/Recurso_291mdpi.png",
            // width: Get.width * 1,
            // height: (Get.width / Get.height) * 35,
          ),
        ),
        Padding(
            padding:
                EdgeInsets.only(top: Get.height * 0.0, left: Get.width * 0.0),
            child: child),
      ],
    );
  }
}
