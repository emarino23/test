import 'package:flutter/material.dart';
import '../index.dart';
import 'package:naver_crs/index.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';

// ignore: must_be_immutable
class CustomBodyDaysWidget extends HookWidget {
  final ExperiencesController ctrl;
  final ValueNotifier<int> counter;
  const CustomBodyDaysWidget({
    Key? key,
    required this.ctrl,
    required this.counter,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    ctrl.state.memory = globalctx.memory;

    return Stack(
      children: [
        Padding(
          padding:
              EdgeInsets.only(top: Get.height * 0.75, left: Get.width * 0.68),
          child: CustomFooterWidget(ctrl: ctrl, counter: counter),
        ),
        Padding(
          padding:
              EdgeInsets.only(top: Get.height * 0.065, left: Get.width * 0.0),
          child: CustomContentWidget(ctrl: ctrl),
        ),
        Obx(() {
          var currentLeftHours = leftHours[currentDay.value] ?? 0.obs;
          return Padding(
            padding: EdgeInsets.only(
                top: Get.height * 0.875, left: Get.width * 0.05),
            child: Text(
              currentLeftHours.value < 0
                  ? "You have exceeded the maximum hours planned for this day !!!"
                  : '',
              style: KTextSytle(
                context: context,
                fontSize: 12,
                fontWeight: FontWeight.bold,
                color: Color.fromARGB(255, 204, 164, 61),
              ).getStyle(),
            ),
          );
        }),
      ],
    );
  }
}
