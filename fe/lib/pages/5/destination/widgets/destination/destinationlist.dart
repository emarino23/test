// ignore_file: file_names
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class DestinationListWidget extends StatelessWidget {
  DestinationListWidget({
    Key? key,
    required this.children,
  }) : super(key: key);
  final children;
  final _scrollController = ScrollController();
  @override
  Widget build(BuildContext context) {
    return Positioned(
      top: Get.height * 0.15,
      left: Get.width * 0.05,
      child: Column(
        children: [
          Container(
              width: Get.width * 0.425,
              height: Get.height * 0.7,
              decoration: const BoxDecoration(
                  borderRadius: BorderRadius.only(
                      bottomRight: Radius.circular(60),
                      bottomLeft: Radius.circular(60),
                      topRight: Radius.circular(60))),
              child: Scrollbar(
                  thumbVisibility: true,
                  thickness: 10,
                  radius: Radius.circular(40),
                  controller: _scrollController,
                  child: SingleChildScrollView(
                      controller: _scrollController,
                      child: Wrap(children: children)))),
        ],
      ),
    );
  }
}
