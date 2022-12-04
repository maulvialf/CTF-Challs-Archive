DROP TABLE IF EXISTS spell_service;
CREATE TABLE spell_service (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    email VARCHAR(255) DEFAULT NULL,
    track_uuid VARCHAR(255) DEFAULT NULL
);

DROP TABLE IF EXISTS tracker;
CREATE TABLE tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    uuid VARCHAR (255) NOT NULL,
    y_coordinate VARCHAR(255) NOT NULL,
    x_coordinate VARCHAR(255) NOT NULL,
    live_spell INTEGER NOT NULL
);
INSERT INTO tracker (uuid, y_coordinate, x_coordinate, live_spell)
VALUES
    ("bbca3ab0-6fc2-48e5-9591-3ac4e470ea58", "226", "420", 0),
    ("c7d7a5bd-4294-443e-8d9a-386fd25b468f", "321", "462", 0),
    ("1c5b70b6-f067-4fcf-9c57-61090d99ec47", "505", "115", 0),
    ("b5da1104-c62b-4283-b66f-0a2f7c82a156", "455", "375", 0),
    ("72911298-84a4-47f6-9954-853de1e2e583", "150", "333", 0),
    ("0b89c6c7-d0ab-4946-9a29-318db739bb5d", "612", "325", 0),
    ("7aba4c89-0fb6-44d3-8968-8cf494d89389", "476", "182", 0),
    ("ad19b07f-07d3-4720-a2ba-c7c367d31a0d", "656", "178", 0),
    ("231dbd3a-3ad5-463a-a921-ae220cf629fe", "336", "574", 0),
    ("50839c5e-12df-41ab-950c-abd824fed616", "228", "582", 0),
    ("005509e0-8c9d-44df-b4ae-dcd69826b39d", "112", "532", 0),
    ("7af4d118-42e5-4c5d-bdb1-ff629a7aab8c", "379", "637", 0),
    ("26e0a15e-fa93-4a7a-b72a-c628bcb976cc", "272", "738", 0),
    ("dd9a5037-0e79-4211-aefa-432ba83562d7", "187", "848", 0),
    ("5a66dd61-a0ce-405c-8899-307fbd69755c", "722", "783", 0),
    ("2d43017a-b446-4a4d-84ca-55843c4ab260", "578", "570", 0),
    ("70e87f37-70be-45cd-8d4f-b6702999f92f", "747", "560", 0),
    ("c1083a45-cc4b-4e71-8047-d9d487801086", "687", "565", 0),
    ("71bbd392-fcdf-4d48-a82a-bc1c68664d69", "597", "730", 0),
    ("64633c83-719b-4a45-a1b5-d2985788438f", "605", "887", 0),
    ("ec10695c-98a8-4e72-b8ad-8916c7a76ed8", "381", "1122", 0),
    ("de19b71c-ebd4-47a9-b229-62c5c7c5cd5b", "496", "1088", 0),
    ("e5a8bd2a-d207-43cd-b233-dcce11a2237f", "476", "732", 0),
    ("d2b573fa-570f-411a-8ba4-d77f0d1a9c25", "130", "339", 0),
    ("4f09ebec-fc2d-4756-837f-3bff796a5ce6", "186", "395", 0),
    ("233adcd7-4342-4dcd-8390-6c370f85b372", "279", "361", 0),
    ("0e51b666-bd1c-4d24-b87a-142a67f0b380", "341", "429", 0),
    ("e79593f2-e39b-4f70-8bee-465f9f2edb42", "471", "335", 0),
    ("4d2c8d93-6a39-4a3a-b319-3008c2ad20bf", "511", "418", 0),
    ("a1754441-ff0a-4fc4-8ea7-176b284dd595", "376", "333", 0),
    ("5c1d5230-aadf-43a5-baab-3fcbe0c944ef", "436", "223", 0),
    ("b50b30c7-d263-4974-bcc7-e9ea8af27be3", "476", "90", 0),
    ("e691cca0-fb5e-48fa-9f21-e8cd703a5fb8", "557", "146", 0),
    ("56729c3c-7215-4df2-b8a5-c9332c9f7a7f", "685", "180", 0),
    ("8e2dd410-a961-4102-8853-b3b4a9b4d2fb", "594", "284", 0),
    ("6fff4b9a-59e8-40be-9118-20cc3fb4ab96", "726", "328", 0),
    ("589027db-8975-4295-ba59-d8230086af46", "686", "419", 0),
    ("5b17cf2d-109a-49e3-a342-3f2c47fae0e1", "622", "455", 0),
    ("b87b1753-f746-44bf-be10-59b51502fbf3", "248", "510", 0),
    ("81515a87-a381-41cf-9935-a5a437d7e795", "191", "535", 0),
    ("54ffd666-5d2c-4658-ac47-bbf492550d2c", "162", "568", 0),
    ("0796b23b-3982-49dc-a212-3eae1e414fa7", "92", "542", 0),
    ("aed06258-711c-483c-9dda-87e47d93cb47", "182", "610", 0),
    ("1369b01b-2930-4e83-b5c0-ceb21ae360ff", "197", "660", 0),
    ("e0dbbac6-9845-4cda-8b3d-e7f534414147", "284", "665", 0),
    ("74cbbf4c-82fa-4834-8ed5-ed1f329d9daa", "178", "750", 0),
    ("32f55007-d160-4c13-b0ba-3b05a502cfb6", "208", "873", 0),
    ("0486700d-d44d-43a4-b536-86a50ca68518", "345", "640", 0),
    ("5cfa7e47-f542-431a-b7e9-73faf9886062", "327", "623", 0),
    ("ade0366c-43ab-4df3-b0c7-fc7f12a43515", "436", "697", 0),
    ("a5992384-2d24-4d93-8620-c313533a9019", "584", "533", 0),
    ("4fd402de-3941-476b-9cf2-67bf0ee349fd", "598", "625", 0),
    ("7d23f305-b2ff-4666-95f4-a9faecc67dc9", "650", "596", 0),
    ("6fa4e8e9-6acc-414b-84a3-4df809601bb3", "655", "532", 0),
    ("89b30a23-8f0a-4acf-b4a6-d7e788bb0447", "708", "527", 0),
    ("03926562-b220-4bf8-b84a-f618986e5d49", "661", "643", 0),
    ("2c298cef-599e-41ca-b9d6-6c75d13b4ce4", "735", "498", 0),
    ("18332bb6-d9ac-4ed4-a3c9-78518b5b1a5f", "678", "729", 0),
    ("8e11cca0-4bb8-495a-b67e-0e7408eafc29", "759", "743", 0),
    ("f6dde622-8578-441e-8485-2328001df6e1", "571", "714", 0),
    ("9df3801a-f71c-4423-a009-c22bd157b2ed", "753", "785", 0),
    ("c9af2471-6030-4668-a40a-032abc75c250", "553", "785", 0),
    ("44d7bacf-aa66-4ff2-b49c-1058bb8dd7f3", "640", "810", 0),
    ("07a2d04b-1023-4bb4-8c35-59a4d5f29401", "602", "963", 0),
    ("48c24298-c409-4cff-842e-e0dd21356e41", "570", "857", 0),
    ("e4b153ab-5912-4f63-addb-40b72db4e30c", "494", "703", 0),
    ("a60be7e5-a815-41f4-8ad5-7e5894269448", "524", "917", 0),
    ("e40559b8-4506-489f-a158-00eae6c4563c", "468", "984", 0),
    ("b729f608-42c7-4583-ba09-c25a5e8b26b4", "479", "1030", 0),
    ("0e293690-f425-446d-b0d8-376db7704f14", "455", "1023", 0),
    ("bb1afcef-be76-4b47-9c82-b0584a7ff06e", "420", "1039", 0),
    ("2a6f983b-bebd-410f-b0a9-8100d4662d3f", "406", "1045", 0),
    ("2983c2f9-2328-461d-92a7-600d0c5083e7", "549", "1074", 0),
    ("c5114722-7e0d-430d-b308-e2e0968b004f", "522", "1166", 0),
    ("5456936e-b1a1-41ee-9887-5e3fb664ab53", "492", "1092", 0),
    ("3b24334e-7d72-443d-ae0b-9fc53cf37f19", "381", "1096", 0),
    ("0165d248-be52-4a72-946c-b2a0be675cb6", "230", "120", 0),
    ("dd1bf485-eab4-4d36-9db4-b498c4f71d44", "60", "520", 0),
    ("ab787b15-e9f9-46dd-9833-c015aedc7131", "400", "110", 0),
    ("e82e3c59-1c3c-45e4-8159-f894cbc10803", "476", "540", 0),
    ("6bdae7cc-f76f-4225-8cfa-aedc9f450201", "406", "780", 0),
    ("0d8c10c0-176b-4d43-badb-9a37a88b5a78", "792", "420", 0),
    ("3d7c3d2f-7b9d-4951-abf5-558ffaaddd9d", "742", "1105", 0);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(255) DEFAULT NULL,
    password VARCHAR(255) DEFAULT NULL
);
INSERT INTO user (username, password) VALUES ("admin", "admin");