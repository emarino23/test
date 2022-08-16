// ignore: must_be_immutable
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../index.dart';
import 'index.dart';
import 'package:naver_crs/index.dart';

// ignore: must_be_immutable
class DestinationsOrderableListWidget extends StatelessWidget {
  const DestinationsOrderableListWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Null Function(String key) onAccept;

    onAccept = (String destination) {
      dragDestination(destination);
    };

    return Padding(
        padding: EdgeInsets.only(
          top: Get.height * 0.0,
          left: Get.width * 0.45,
        ),
        child: DestinationDragTargetWidget(onAccept: onAccept));
  }
}
