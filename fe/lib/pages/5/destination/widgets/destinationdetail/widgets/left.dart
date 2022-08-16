import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';

class DestinationDetailLeftWidget extends StatelessWidget {
  const DestinationDetailLeftWidget({
    Key? key,
    required this.destination,
    required this.index,
  }) : super(key: key);

  final destination;
  final index;

  @override
  Widget build(BuildContext context) {

    return GalleryWidget(destination: destination);
  }
}
