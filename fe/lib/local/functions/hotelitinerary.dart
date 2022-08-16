import 'package:flutter/material.dart';
import '../../index.dart';

class HotelItineraryWidget extends StatelessWidget {
  const HotelItineraryWidget({
    Key? key,
    required this.row,
  }) : super(key: key);
  final row;
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        children: [
          Text(
            "${row["value"]['roomcategory']}",
            style: KTextSytle(
              context: context,
              fontSize: 12,
              fontWeight: FontWeight.bold,
              color: Color.fromARGB(255, 204, 164, 61),
            ).getStyle(),
          ),
          TextButton(
              onPressed: () {
                showCustomDialog(
                    context,
                    YoutubeWidget(
                      videoId: row["value"]["video"],
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
          Text(
            "${row["value"]['roomdescription']}",
            style: KTextSytle(
              context: context,
              fontSize: 12,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ).getStyle(),
          ),
          LeftGalleryWidget(
              catalog: "hotel", code: row["code"], value: "images"),
        ],
      ),
    );
  }
}
