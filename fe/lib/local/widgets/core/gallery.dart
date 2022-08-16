// ignore_for_file: non_constant_identifier_names

import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';
import '../../../pages/5/destination/widgets/dgallery/index.dart';

class GalleryWidget extends GetView<DGalleryController> {
  final destination;
  const GalleryWidget({Key? key, this.destination}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var destData = getDestinationValueByName(destination);

    return SizedBox(
      width: Get.width * 0.4,
      child: Column(
        children: [
          Wrap(
            children: [
              Text(destination.toString().toUpperCase(),
                  style: KTextSytle(
                          context: context,
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: Colors.white)
                      .getStyle()),
              TextButton(
                  onPressed: () {
                    showCustomDialog(
                        context,
                        YoutubeWidget(
                          videoId: destData["video"],
                        ),
                        "Close",
                        backgroundColor: Color.fromARGB(100, 0, 0, 0),
                        buttonColor: Colors.white);
                  },
                  child: Text("    click here to watch video",
                      style: KTextSytle(
                              context: context,
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                              color: Colors.grey)
                          .getStyle())),
            ],
          ),
          Wrap(
            children: [
              Text("${destData["data"][8]}",
                  style: KTextSytle(
                          context: context,
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                          color: Colors.grey)
                      .getStyle()),
            ],
          ),
          SizedBox(height: Get.height * 0.1),
          SizedBox(
            height: Get.height * 0.5,
            child: Obx(() => LeftGalleryWidget(
                catalog: "destinations",
                code: globalDestinationCode.value,
                value: "tour_images")),
          ),
        ],
      ),
    );
  }
}
