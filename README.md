# Import OBJ from Trainz

## Introduction

"Import OBJ from Trainz" is an addon for Blender that allows you to import `.obj` files from the Trainz game. The addon performs several operations upon import:
- Rotates the object by -90 degrees along the X-axis.
- Rotates the UV mapping by 180 degrees and mirrors the UVs along the X-axis.
- Processes an associated `.ms` (MaxScript) file that contains attachment nodes and adds them to the scene.

## Installation

### 1. Download the Addon

Download the Python script file (e.g., `import_obj_from_trainz.py`) from the provided source.

### 2. Install the Addon in Blender

1. Open Blender.
2. Go to `Edit` > `Preferences` > `Add-ons`.
3. Click the `Install` button at the top and select the downloaded `.zip` file.
4. After installation, ensure that the "Import OBJ from Trainz" addon is enabled in the addon list.

### 3. Enable the Addon

Once the addon is installed and enabled, you will see the "Import OBJ from Trainz" panel under the `Import` tab in the 3D View.

## Usage

1. **Open Blender and Enable the Addon**  
   After enabling the addon, you’ll find the "Import OBJ from Trainz" panel in the `Import` tab in the 3D Viewport.

2. **Import `.obj` File**
   - In the panel, click the `OBJ File` field to select your `.obj` file.
   - Click the `MS File` field to select the corresponding `.ms` file (with attachment nodes).

3. **Import and Process**
   - Click the `Import OBJ from Trainz` button to import the `.obj` file. The addon will:
     - Rotate the object by -90 degrees along the X-axis.
     - Rotate the UV mapping by 180 degrees and mirror it along the X-axis.
     - Process the `.ms` file and create attachment nodes in the scene.

4. **Finished Import**
   The object and its attachment nodes will be added to the scene and you can start editing or adjusting them as needed.

## Addon Panel

In the 3D View’s right panel, you will find the **Import OBJ from Trainz** panel under the `Import` tab. This panel includes the following options:
- **OBJ File**: Select the `.obj` file to import.
- **MS File**: Select the `.ms` file containing the attachment node data.
- **Import OBJ from Trainz**: Click this button to import and process the files.

## Features Overview

- **Import `.obj` Files**: The addon will load the `.obj` file and import it into the current Blender scene.
- **Rotate Model**: The model is rotated -90 degrees along the X-axis to match the Trainz model's orientation.
- **Adjust UVs**: The UV coordinates will be rotated by 180 degrees and mirrored along the X-axis to fit the Trainz texture mapping.
- **Process `.ms` File**: The addon will parse the `.ms` file and extract attachment node data, creating empty objects at those positions in Blender.

## Notes

- **Converting `.im` or `.trainzmesh` Files**:  
  If you have `.im` or `.trainzmesh` files instead of `.obj`, you need to convert them to `.obj` format using **3D Object Converter** before using this addon in Blender.

- Ensure that the `.obj` and `.ms` files are in the same directory, and that you have specified the correct file paths in the addon.

- The `.ms` file format should be compatible with the regular expression in the addon. If your `.ms` file has a different structure, you may need to modify the regex to match your file format.

## Troubleshooting

### Q1: The imported model doesn’t look correct. What should I do?
A1: Ensure that the `.obj` file is correctly exported and that the `.ms` file matches the object. If the problem persists, check that the UVs and geometry data in the `.obj` file are correct.

### Q2: How do I adjust the position of the attachment nodes?
A2: The position of attachment nodes is determined by the `.ms` file. You can manually adjust the empty objects (attachment nodes) in Blender if needed.

### Q3: The UV adjustments don’t match my needs. Can I change them?
A3: The addon automatically rotates and mirrors UVs. If this doesn't fit your requirements, you can manually adjust the UVs in Blender or modify the addon’s UV processing code.

## Developer Contact

If you encounter any issues or have suggestions for improvements, feel free to contact the author:
- Author: Your Name
- Email: [YourEmail@example.com]

---

# Import OBJ from Trainz 插件

## 简介

"Import OBJ from Trainz" 是一个 Blender 插件，允许您导入 Trainz 游戏的 `.obj` 文件。插件会在导入时执行一系列操作：
- 沿 X 轴旋转模型 -90 度。
- 旋转 UV 映射 180 度，并沿 X 轴镜像 UV。
- 解析与 `.obj` 文件同目录下的 `.ms`（MaxScript）文件，添加附加节点到场景中。

## 安装

### 1. 下载插件

从提供的源下载 Python 脚本文件（例如 `import_obj_from_trainz.py`）。

### 2. 在 Blender 中安装插件

1. 打开 Blender。
2. 进入 `编辑 (Edit)` > `偏好设置 (Preferences)` > `插件 (Add-ons)`。
3. 点击顶部的 `安装 (Install)` 按钮，选择下载的 `.zip` 文件。
4. 安装完成后，确保插件 "Import OBJ from Trainz" 已启用。

### 3. 启用插件

插件安装并启用后，您会在 Blender 3D 视图的 `导入 (Import)` 标签下看到 "Import OBJ from Trainz" 面板。

## 使用步骤

1. **打开 Blender 并启用插件**  
   启用插件后，您将在 3D 视图的 `导入 (Import)` 标签下看到 "Import OBJ from Trainz" 面板。

2. **导入 `.obj` 文件**
   - 在面板中，点击 `OBJ 文件 (OBJ File)` 字段选择您的 `.obj` 文件。
   - 点击 `MS 文件 (MS File)` 字段选择与 `.obj` 文件同目录下的 `.ms` 文件。

3. **导入并处理**
   - 点击 `Import OBJ from Trainz` 按钮，插件将导入 `.obj` 文件并执行以下操作：
     - 沿 X 轴旋转模型 -90 度。
     - 旋转 UV 坐标 180 度，并沿 X 轴镜像。
     - 解析 `.ms` 文件并在场景中创建附加节点。

4. **完成导入**
   导入的对象和附加节点将出现在场景中，您可以继续编辑或调整它们。

## 插件面板

在 3D 视图的右侧面板中，您会看到 `Import OBJ from Trainz` 面板，该面板包含以下选项：
- **OBJ 文件 (OBJ File)**: 选择 `.obj` 文件。
- **MS 文件 (MS File)**: 选择包含附加节点数据的 `.ms` 文件。
- **Import OBJ from Trainz**: 点击此按钮导入并处理文件。

## 功能概述

- **导入 `.obj` 文件**: 插件会加载 `.obj` 文件并导入到当前 Blender 场景。
- **旋转模型**: 模型将沿 X 轴旋转 -90 度，使其符合 Trainz 模型的方向。
- **调整 UV 坐标**: 插件会将 UV 坐标旋转 180 度，并沿 X 轴镜像，适应 Trainz 的纹理映射。
- **处理 `.ms` 文件**: 插件会解析 `.ms` 文件并提取附加节点数据，在 Blender 中创建空物体表示这些附加节点。

## 注意事项

- **转换 `.im` 或 `.trainzmesh` 文件**:  
  如果您有 `.im` 或 `.trainzmesh` 文件，而不是 `.obj` 文件，您需要使用 **3D Object Converter** 工具将其转换为 `.obj` 格式，然后才能在 Blender 中使用此插件。

- 确保 `.obj` 文件和 `.ms` 文件在同一目录下，并且已正确指定文件路径。

- `.ms` 文件格式应与插件中的正则表达式匹配。如果 `.ms` 文件结构不同，可能需要修改插件代码中的正则表达式部分以适应实际情况。

## 常见问题解答（FAQ）

### Q1：导入的模型看起来不对，怎么解决？
A1：请确保导入的 `.obj` 文件正确，且 `.ms` 文件与 `.obj` 文件匹配。如果问题仍然存在，请检查 `.obj` 文件中的 UV 和几何数据。

### Q2：如何调整附加节点的位置？
A2：附加节点的位置是根据 `.ms` 文件自动设置的。如果需要调整位置，您可以在 Blender 中手动编辑这些空物体。

### Q3：UV 坐标调整后不符合预期，如何修复？
A3：插件会自动旋转并镜像 UV 坐标。如果这种方式不符合您的需求，您可以在 Blender 中手动调整 UV，或者修改插件中的 UV 处理代码。

## 插件开发者联系方式

如遇问题或有改进建议，欢迎与作者联系：
- 作者：Your Name
- 联系邮箱：[YourEmail@example.com]
