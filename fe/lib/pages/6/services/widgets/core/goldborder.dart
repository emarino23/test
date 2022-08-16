import 'package:flutter/material.dart';
import 'package:get/get.dart';

class GoldBorderWidget extends StatelessWidget {
  const GoldBorderWidget({Key? key, required this.child}) : super(key: key);
  final Widget child;
  @override
  Widget build(BuildContext context) {
    return Container(
        width: Get.width * 0.4,
        height: Get.height * 0.11,
        decoration: BoxDecoration(
          image: DecorationImage(
            image: Image.asset(
              "assets/images/1x/Recurso_211mdpi.png",
              width: Get.width * 0.1,
              fit: BoxFit.fill,
            ).image,
          ),
        ),
        child: Stack(
          children: [
            Center(child: child),
          ],
        ));
  }
}
